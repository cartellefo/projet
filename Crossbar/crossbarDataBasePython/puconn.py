###############################################################################
#
# Copyright (C) 2014, Tavendo GmbH and/or collaborators. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
###############################################################################
#import psycopg2
import time
import os
import argparse
import six
import txaio
import json
import numpy
import sys
from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.util import sleep
from datetime import datetime
from twisted.internet.task import LoopingCall
from twisted.internet import reactor
from twisted.logger import Logger


from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner


class Zaehler(ApplicationSession):

    def onConnect(self):
        self.log.info("Client connected")
        self.join(self.config.realm, [u'anonymous'])

    def onChallenge(self, challenge):
        self.log.info(
            "Challenge for method {authmethod} received", authmethod=challenge.method)
        raise Exception("We haven't asked for authentication!")

    @inlineCallbacks
    def onJoin(self, details):
        print('on join')

        @inlineCallbacks
        def _cpuload(): # fonction to calculated the cpu time
            start = time.time()
            print(' please give me the CPU time')
            end = time.time()
            elapsed = end - start # cpu time 
            # my_payload is the data to published
            my_payload = {
                         'tsp': datetime.utcnow().isoformat(), 
                         'piid': 'none', 
                         'elapsed': elapsed
                         }

            print('sending payload:  {}'.format(my_payload))
            yield self.publish(u'repi.data.simple.gaussian', my_payload)# publisher my_payload

            #print('cpu time is ',elapsed)
            yield sleep(1)
            return(elapsed)
            

        print('Starte Messung')
        i = 0

        while i < 100:
            yield _cpuload()
            # print('cpu time is ', _cpuload())
            # yield _do2()
            yield sleep(1)
            i = i+1

        @inlineCallbacks
        def _do():
            self.counter = self.counter + 1 
            uu = numpy.random.normal(self.mean, self.variance)
            yield self.publish(u're.data.simple.'+self.id+'.gaussian', {'tsp': datetime.utcnow().isoformat(), 'val':uu, 'piid':self.id})
            if self.counter > 60*self.timeinterval:
                self.counter=1
                print(uu)
            return

        # yield self.publish(u're.data.simple.'+self.id+'.gaussian', {'tsp': datetime.utcnow().isoformat(), 'val':uu, 'piid':self.id})
        self.lc = LoopingCall(_do)
        self.lc.start(1)

       
    def onLeave(self, details):
        self.log.info('session left: {}'.format(details))

        self.disconnect()

    def onDisconnect(self):
        self.log.info('transport disconnected')


if __name__ == '__main__':

    print('parse command line parameters')
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--debug', action='store_true',help='Enable debug output.')
    parser.add_argument('--url', dest='url', type=six.text_type, default=u'ws://localhost:8080/ws', help='The router URL (default: "ws://104.199.76.81:8080/ws").')
   
    parser.add_argument('--realm', dest='realm', type=six.text_type,
                        default='realm1', help='The realm to join (default: "realm1").')

    args = parser.parse_args()
    print(args)
    # now actually run a WAMP client using our session class ClientSession
    runner = ApplicationRunner(url=args.url, realm=args.realm)
    print(runner)
    runner.run(Zaehler, auto_reconnect=True)

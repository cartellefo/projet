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

import os
import argparse
import six
import txaio
import json
import time
import numpy
import sys
from coalesce import coalesce
import psycopg2
from twisted.internet.defer import inlineCallbacks, returnValue
from datetime import datetime
from autobahn.wamp.types import SubscribeOptions
# from twisted.internet.task import LoopingCall
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
        try:
            conn = psycopg2.connect(
                "dbname='postgres' user='postgres' host='localhost' password='dbpass'")
            cur = conn.cursor()
            print('Connection was successful. ')
        except Exception as e:
            raise e
        # hhier muss code für subscriptioon hin

        def write_msg_simple(msg, details):

            print("event for write_msg received: {}".format(msg))
            print("details for write_msg received: {}".format(details))

            if details.topic == 'repi.data.extrema':
                print(msg['tsp'], msg['extrema'], ((str(details).split(',')[6]).split('.')[2])[
                      :-1], (str(details).split(',')[2]).split('=')[1])
            else:
                print(msg['tsp'], msg['elapsed'], ((str(details).split(',')[6]).split('.')[2])[
                      :-1], (str(details).split(',')[2]).split('=')[1])

            write_msg(msg)
            #read_msg(msg)

            #    infos = ((str(details).split(',')[6]).split('.')[2])[:-1]
            #    print(infos)
            #     
            #            hier soll nun daten ausggeben werden format:
            # topic (elased time oder extrma), publication number wert, tsp

        # def write_msg(msg):
        #     print("event for write_msg received: {}".format(msg))
        #     sql = """INSERT INTO vendors (vendor_name) VALUES(%s) """
        #     print(sql % str(msg['elapsed']))
        #     cur.execute(sql, (msg['elapsed'],))
        #     # id = cur.fetchone()[0]
        #     conn.commit()
        #     return(1)

        def write_msg(msg):
            print("event for write_msg received: {}".format(msg))
            sql = """INSERT INTO employee (empl_name) VALUES(%s) """
            print(sql % str(msg['elapsed']))
            cur.execute(sql, (msg['elapsed'],))
            # id = cur.fetchone()[0]
            conn.commit()
            return(1)






        # def read_msg(msg):
        #     print("event for read_msg received: {}".format(msg))
        #     sql = """  INSERT INTO stadt (nachname, vorname)
        #     SELECT code, nom
        #     FROM animal
        #     WHERE animal.code > %i"""
        #     cur.execute(sql%(msg['elapsed'],))
        #     conn.commit()
        #     return(1)

        # wildcards
        # session.subscribe("com.mychatapp.privatechannel..statusupdate", monitorStatusUpdates, { match: "wildcard" });

        # sub = yield self.subscribe("u'repi.data.elapsed_time'.u'repi.data.extrema'",write_msg_simple)

        # sub = yield self.subscribe(write_msg_simple, u'repi.data.extrema.repi.data.elapsed_time')
        # sub = yield self.subscribe(u'repi.data',write_msg_simple, { match: "prefix" });
        # sub = yield self.subscribe( write_msg_simple, u"repi.data", options=SubscribeOptions(match=u"prefix", details_arg=u"details") );
        sub = yield self.subscribe(write_msg_simple, u"repi.data", options=SubscribeOptions(match=u"prefix", details_arg="details"))

        # sub = yield self.subscribe(write_msg_simple, u'repi.data.elapsed_time')
        # print("procedure write_msg() 'write to the data base'")

        # sub = yield self.subscribe(write_msg_simple, u'repi.data.extrema')
        # print("procedure write_msg() 'write to the data base'")

        def read_msg(msg):
            print("event for read_msg send: {}".format(msg))
            sql = """SELECT vendor_name FROM vendors  WHERE vendor_id <=100 """
            # sql = """SELECT p_alter FROM t_players  WHERE p_alter <=100 """
            cur.execute(sql)
            # row = cur.fetchall()
            # print(row)
            # cur.execute("""SELECT vendor_name FROM vendors WHERE vendor_id =10 """)
            x = cur.fetchall()
            print(x)
        ################################################################################

            # sql = """SELECT vendor_id, vendor_name FROM vendors ORDER BY vendor_name limit (%s)) """
            # cur.execute(sql, msg ...) #
            # print("The number of parts: ", cur.rowcount)
            # row = cur.fetchall()
            # print(row)
            # rows=row
            # while row is not None:
            #    print(row)
            #    row = cur.fetchone()
        ###############################################################

            return(x)
        read_msg('hello')

        reg = yield self.register(read_msg, u'repi.data.select')
        print("procedure read_msg() read to the data base")

   

    def onLeave(self, details):
        self.log.info('session left: {}'.format(details))

        self.disconnect()

    def onDisconnect(self):
        self.log.info('transport disconnected')


if __name__ == '__main__':

    print('parse command line parameters')
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--debug', action='store_true',
                        help='Enable debug output.')
    parser.add_argument('--url', dest='url', type=six.text_type, default=u'ws://localhost:8080/ws',
                        help='The router URL (default: "ws://104.199.76.81:8080/ws").')
#    parser.add_argument('--router', type=six.text_type,default=u'ws://104.199.76.81:8080/ws',help='WAMP router URL.')

#    parser.add_argument('--realm',type=six.text_type, default='realm1',help='WAMP router realm.')
    parser.add_argument('--realm', dest='realm', type=six.text_type,
                        default='realm1', help='The realm to join (default: "realm1").')

    args = parser.parse_args()
    print(args)
    # now actually run a WAMP client using our session class ClientSession
    runner = ApplicationRunner(url=args.url, realm=args.realm)
    print(runner)
    runner.run(Zaehler, auto_reconnect=True)

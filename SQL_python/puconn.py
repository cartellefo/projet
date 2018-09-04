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
import os
import argparse
import six
import txaio
import json
import numpy 
import sys
from twisted.internet.defer import inlineCallbacks, returnValue
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
        self.log.info("Challenge for method {authmethod} received", authmethod=challenge.method)
        raise Exception("We haven't asked for authentication!")

    @inlineCallbacks
    def onJoin(self, details):
        print('on join')

        @inlineCallbacks
        def _do():
            #uu = numpy.random.normal(0, 2)
            
         #   yield self.publish(u'repi.data.simple.gaussian', {'tsp': datetime.utcnow().isoformat(), 'val':uu, 'piid':'none'}) 
            yield self.publish(u'repi.data.simple.gaussian', 'hi') #{'tsp': datetime.utcnow().isoformat(), 'piid':'none'}, {'excludeMe': False})  
            yield sleep(1)   
            returnValue(2)

        @inlineCallbacks
        def _do2():
            #uu = numpy.random.normal(0, 2)
            
         #   yield self.publish(u'repi.data.simple.gaussian', {'tsp': datetime.utcnow().isoformat(), 'val':uu, 'piid':'none'}) 
            self.publish(u'repi.data.simple.gaussian', {'tsp': datetime.utcnow().isoformat(), 'piid':'none'})    
            yield sleep(1) 
            return(1)

            hello(args)
            print(args) 





        def connect():
            
            conn = None
            try:
                
                print('Connecting to the PostgreSQL database...')
                conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='dbpass'")
                cur = conn.cursor()
                print('PostgreSQL database version:')
                cur.execute('SELECT version()')
                db_version = cur.fetchone()
                print(db_version)
               
             
                cur.close()
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
            finally:
                if conn is not None:
                    conn.close()
                    print('Database connection closed.')


        

        def insert_vendor(vendor_name):
            """ insert a new vendor into the vendors table """
            sql = """INSERT INTO vendors(vendor_name)
                     VALUES(%s) RETURNING vendor_id;"""
            conn = None
            vendor_id = None
            try:
                
                conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='dbpass'")
                
                cur = conn.cursor()
                
                cur.execute(sql, (vendor_name,))
                
                vendor_id = cur.fetchone()[0]
                
                conn.commit()
                
                cur.close()
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
            finally:
                if conn is not None:
                    conn.close()
         
            return vendor_id

        connect()
        insert_vendor('cartelle inc')    
# sub = yield self.subscribe(onhello, 'com.example.onhello')       

# sub = yield self.subscribe(onhello, 'com.example.onhello')
        
        print('Starte Messung')

  #      self.lc = LoopingCall(_do)
  #      self.lc.start(1)
        i=0

       # while i < 10:
            #yield self.publish(u'repi.data.simple.gaussian', 'hi')
        yield self.publish(u'repi.data.simple.gaussian', {'tsp': datetime.utcnow().isoformat(), 'piid':'aussen!'})    
            
        yield _do2()
        print('hi')
        yield _do2()
        print('hi')
        yield _do2()
        print('hi')
        yield _do2()
        print('him')
        i=i+1

        
    def onLeave(self, details):
        self.log.info('session left: {}'.format(details))

        self.disconnect()

    def onDisconnect(self):
        self.log.info('transport disconnected')


if __name__ == '__main__':

    print ('parse command line parameters')
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--debug', action='store_true', help='Enable debug output.')
    parser.add_argument('--url', dest='url', type=six.text_type, default=u'ws://localhost:8080/ws', help='The router URL (default: "ws://104.199.76.81:8080/ws").')
#    parser.add_argument('--router', type=six.text_type,default=u'ws://104.199.76.81:8080/ws',help='WAMP router URL.')
 
#    parser.add_argument('--realm',type=six.text_type, default='realm1',help='WAMP router realm.')
    parser.add_argument('--realm', dest='realm', type=six.text_type, default='realm1', help='The realm to join (default: "realm1").')

    args = parser.parse_args()
    print(args)
    # now actually run a WAMP client using our session class ClientSession
    runner = ApplicationRunner(url=args.url, realm=args.realm)
    print(runner)
    runner.run(Zaehler, auto_reconnect=True)



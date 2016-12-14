#! /usr/bin/env python

import argparse
import os
from channels import getChannels
from send import sendMessage
from users import getUsers

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Read and send your Slack messages over the command line!')    
    parser.add_argument('-t','--token', help='Use specified token instead of $SLACK_TOKEN')
    subparsers = parser.add_subparsers(title='Commands', dest='subparser_name')

    parser_l = subparsers.add_parser('list', help='List channels and/or users')
    group_l = parser_l.add_mutually_exclusive_group(required=True)
    group_l.add_argument('-a','--all', action='store_true', help='List channels and users')
    group_l.add_argument('-c','--channels', action='store_true', help='List channels')
    group_l.add_argument('-u','--users', action='store_true', help='List users')
    
    parser_r = subparsers.add_parser('read', help='Read messages from a channel')
    parser_r.add_argument('channel', help='The channel or user to read from')
    parser_r.add_argument('-u', '--unread', help='Show only unread messages')

    parser_s = subparsers.add_parser('send', help='Send a message')
    parser_s.add_argument('channel', help='The channel or user to send the message to')
    parser_s.add_argument('message', help='The message text')
    
    args=parser.parse_args()

    #Get Token
    token = args.token if args.token else os.environ.get('SLACK_TOKEN')

    if args.subparser_name == 'list':
        if args.channels: getChannels(token)
        elif args.users: getUsers(token)
        elif args.all: 
            getChannels(token) 
            getUsers(token)

    elif args.subparser_name == 'read':
        print('Coming soon!')

    elif args.subparser_name == 'send':        
         sendMessage(token, args.channel, args.message)

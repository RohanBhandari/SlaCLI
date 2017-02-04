#! /usr/bin/env python

import argparse
from argparse import ArgumentDefaultsHelpFormatter
import os
from src.channels import getChannels
from src.read import readMessages
from src.send import sendMessage
from src.users import getUsers

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Read and send your Slack messages over the command line!')    
    parser.add_argument('-t','--token', help='Use specified token instead of $SLACK_TOKEN')
    subparsers = parser.add_subparsers(title='Commands', dest='subparser_name')

    parser_l = subparsers.add_parser('list', help='List channels and users')
    group_l = parser_l.add_mutually_exclusive_group(required=False)
    group_l.add_argument('-c','--channels', action='store_true', help='List only channels')
    group_l.add_argument('-u','--users', action='store_true', help='List only users')

    parser_r = subparsers.add_parser('read', help='Read messages from a channel')
    parser_r.add_argument('channel', help='The channel or user to read from')
    parser_r.add_argument('-u', '--unread', help='Show only unread messages')
    parser_r.add_argument('num', default='10', help='Number of messages to display. Default is 10')

    parser_s = subparsers.add_parser('send', help='Send a message')
    parser_s.add_argument('channel', help='The channel or user to send the message to')
    parser_s.add_argument('message', help='The message text')
    
    args=parser.parse_args()

    #Get Token
    token = args.token if args.token else os.environ.get('SLACK_TOKEN')

    if args.subparser_name == 'list':
        if args.channels: getChannels(token)
        elif args.users: getUsers(token)
        else: 
            getChannels(token) 
            getUsers(token)

    elif args.subparser_name == 'read':
        readMessages(token, args.channel, args.num)

    elif args.subparser_name == 'send':        
         sendMessage(token, args.channel, args.message)

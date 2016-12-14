import argparse
import os
from channels import getChannels
from send import sendMessage
from users import getUsers


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Read and send your Slack messages over the command line!')    
    parser.add_argument('-t','--token', help='Use specified token instead of $SLACK_TOKEN')
    subparsers = parser.add_subparsers(help='Commands')
    
    #Need to change subparsers to groups
    parser_s = subparsers.add_parser('send', help='Send a message')
    parser_s.add_argument('channel', help='The channel to send the message to')
    parser_s.add_argument('message', help='The message text')

    parser_r = subparsers.add_parser('read', help='Read messages from a channel')
    parser_r.add_argument('channel', help='The channel to read')
    parser_r.add_argument('-u', '--unread', help='Show only unread messages')

    #These need to be exclusive argument.
    parser_l = subparsers.add_parser('list', help='List channels or users')
    parser_l.add_argument('--channels', action='store_true', help='List channels')
    parser_l.add_argument('--users', action='store_true', help='List users')
    parser_l.add_argument('--all', action='store_true', help='List channels and users')
    
    args=parser.parse_args()

    #Get Token
    token = args.token if args.token else os.environ.get('SLACK_TOKEN')

#    if args.message:
#        sendMessage(token, args.channel, args.message)
#    elif args.read:
#        print('I read good!')
#    elif args.list:
    if args.channels:
        getChannels(token)
    elif args.users:
        getUsers(token)
    elif args.all:
        getChannels(token)
        getUsers(token)

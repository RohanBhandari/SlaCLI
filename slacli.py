import argparse
import os
from send import sendMessage

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Read and send your Slack messages over the command line!')    
    subparsers = parser.add_subparsers(help='Commands')

    parser_s = subparsers.add_parser('send', help='Send a message')
    parser_s.add_argument('channel', help='The channel to send the message to')
    parser_s.add_argument('message', help='The message text')

    parser_r = subparsers.add_parser('read', help='Read messages from a channel')
    parser_r.add_argument('channel', help='The channel to read')
    parser_r.add_argument('-u', '--unread', help='Show only unread messages')
    
    args=parser.parse_args()

    #Get Token
    token = os.environ.get('SLACK_TOKEN')
 
    if args.message:
        sendMessage(token, args.channel, args.message)
    elif args.read:
        print('I read good!')

import json
import os
import argparse

def main():
        parser = argparse.ArgumentParser(description='Instagram hoarder pack')

        parser.add_argument('-s', '--saved', action='store_true', help='Download saved posts')
        parser.add_argument('-l', '--liked', action='store_true', help='Download liked posts')
        parser.add_argument('-f', '--following', action='store_true', help='Download all content from Following')

        args = parser.parse_args()

        if not (args.saved or args.liked or args.following):
                parser.error('You must specify at least one of --saved, --liked, or --following')

        base = f'gallery-dl --cookies "{cookies_url}"'
        cookies_url = 'cookies.txt'

        if args.saved:
                posts = json.loads(open('saved_posts.json', 'r').read())['saved_saved_media']
                length = len(posts)

                for index, post in enumerate(posts):
                        print(f'Processing post [{index + 1}/{length}]')
                        os.system(base + f'{post['string_map_data']['Saved on']['href']}')
                        
        if args.liked:
                posts = json.loads(open('liked_posts.json', 'r').read())
                ...

        if args.following:
                profiles = json.loads(open('following.json', 'r').read())
                ...

if __name__ == '__main__':
        main()

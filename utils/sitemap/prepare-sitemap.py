import os, errno
import requests
import argparse
import xml.etree.ElementTree as ET

TMP_FILE_NAME = 'sitemap-tmp.xml'
RESULT_FILE_NAME = 'sitemap-urls.txt'


def parse_args():
    parser = argparse.ArgumentParser()

    required_args_group = parser.add_argument_group('Required arguments')
    required_args_group.add_argument('-u', '--url', help='URL to sitemap.xml', type=str, required=True)
    required_args_group.add_argument('-bu', '--base_url', help='Base site URL', type=str, required=True)

    return parser.parse_args()


def load_tmp_xml(url):
    response = requests.get(url)
    with open(TMP_FILE_NAME, 'wb') as f:
        f.write(response.content)


def remove_tmp_xml():
    try:
        os.remove(TMP_FILE_NAME)
    except OSError as e:
        if e.errno != errno.ENOENT:
            raise


def parse_xml(base_url):
    tree = ET.parse(TMP_FILE_NAME)
    root = tree.getroot()
    urls = []

    for location in root.findall('./xmlns:url/xmlns:loc', {'xmlns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}):
        full_url = location.text
        urls.append(full_url.replace(base_url, ''))

    return urls


def save(items):
    with open(RESULT_FILE_NAME, 'w') as file:
        for line in items:
            file.write(line + "\n")
    file.close()


def main():
    args = parse_args()
    load_tmp_xml(args.url)
    save(parse_xml(args.base_url))
    remove_tmp_xml()


if __name__ == "__main__":
    main()

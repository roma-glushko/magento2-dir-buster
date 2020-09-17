# Magento2 Dir Buster

A list of well-know Magento places that normally should be hidden or protected by server configurations.

## Usage

This list is compatible with commonly-used tools for webfuzzing like GoBuster:

```bash
gobuster dir -u https://www.magento.com/ -w magento2-dir-list.txt -k
```

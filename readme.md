# Magento2 Dir Buster

A list of well-know Magento places that normally should be hidden or protected by server configurations.

## Usage

This list is compatible with commonly-used tools for webfuzzing like GoBuster:

```bash
gobuster dir -u https://www.magento.com/ -w magento2-dir-list.txt -k
```

Also, you can use prepare-sitemap.py util to prepare sitemap.xml to GoBuster scan:

```bash
python utils/sitemap/prepare-sitemap.py -u https://www.example.com/sitemap.xml -bu https://www.example.com/
```

You will get sitemap-urls.txt file with the ready to use urls. To get the report with accessible or not accessible urls:

```bash
gobuster dir -u https://www.example.com/ -w sitemap-urls.txt -v -o gobuster-report.txt
```

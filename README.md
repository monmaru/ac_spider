# ac_spider
Spider on the cloud

## Deploy on Scrapy Cloud
This configuration is done in your local project’s scrapinghub.yml.  
There you have to include a section called stacks having scrapy:1.2-py3 as the stack for your Scrapy Cloud project:
```
projects:
    default: YOUR_PROJECT_ID
stacks:
    default: scrapy:1.2-py3
```
After doing that, you just have to deploy your project using shub:
```
shub deploy
```
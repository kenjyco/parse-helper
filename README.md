## Install

Install system requirements for `lxml`

```
% sudo apt-get install -y libxml2 libxslt1.1 libxml2-dev libxslt1-dev zlib1g-dev
```

> Try `brew install libxml2` if using a Mac.

Install with `pip`

```
% pip install parse-helper
```

## Usage

```python
In [1]: import parse_helper as ph

In [2]: ph.USER_AGENT
Out[2]: 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/58.0.3029.110 Chrome/58.0.3029.110 Safari/537.36'

In [3]: ph.google_serp('scaling redis')
Out[3]:
[{'link': 'https://redis.io/topics/partitioning',
  'title': 'Partitioning: how to split data among multiple Redis instances. – Redis'},
 {'link': 'http://highscalability.com/blog/2014/9/8/how-twitter-uses-redis-to-scale-105tb-ram-39mm-qps-10000-ins.html',
  'title': 'How Twitter Uses Redis to Scale - 105TB RAM ... - High Scalability'},
 {'link': 'http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Scaling.RedisReplGrps.html',
  'title': 'Scaling Redis Clusters with Replica Nodes - Amazon ElastiCache'},
 {'link': 'http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Scaling.RedisStandalone.ScaleUp.html',
  'title': 'Scaling Up Single-Node Redis Clusters - Amazon ElastiCache'},
 {'link': 'https://redislabs.com/ebook/part-3-next-steps/chapter-10-scaling-redis/',
  'title': 'Chapter 10: Scaling Redis - Redis Labs'},
 {'link': 'https://redislabs.com/blog/scaling-out-redis-read-only-slaves-or-cluster/',
  'title': 'Scaling Out Redis: Read-Only Slaves or Cluster? - Redis Labs'},
 {'link': 'http://petrohi.me/post/6323289515/scaling-redis',
  'title': 'ten thousand hours • Scaling Redis'},
 {'link': 'https://www.quora.com/How-scalable-is-Redis',
  'title': 'How scalable is Redis? - Quora'},
 {'link': 'https://www.linkedin.com/pulse/how-twitter-uses-redis-scale-105tb-ram-39mm-qps-10000-iravani',
  'title': 'How Twitter Uses Redis To Scale - 105TB RAM, 39MM QPS ... - LinkedIn'},
 {'link': 'https://docs.microsoft.com/en-us/azure/redis-cache/cache-how-to-scale',
  'title': 'How to Scale Azure Redis Cache | Microsoft Docs'}]
```

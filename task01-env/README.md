目标

环境要求：Python 3.11+、uv

安装：uv sync

运行：uv run python -m async_fetch.cli ... 和 uv run async-fetch ...

输出示例：2026-11-17 15:11:16,443 INFO async_fetch.fetcher start fetch url=https://this-domain-should-not-exist-12345.com
2026-11-17 15:11:16,653 WARNING async_fetch.fetcher failed url=https://this-domain-should-not-exist-12345.com error=[Errno 11001] getaddrinfo failed
[
  {
    "url": "https://this-domain-should-not-exist-12345.com",
    "status": null,
    "length": 0,
    "elapsed": 0.20939910000015516,
    "error": "[Errno 11001] getaddrinfo failed"
  }
]
(task01-env) 

目录结构

设计说明：单 client、asyncio.gather、异常回填、logging

踩坑记录：至少写两条，比如 [project.scripts] 重复、cli.py 没保存导致 ImportError

验收对照
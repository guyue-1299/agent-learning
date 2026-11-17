import argparse
import asyncio
import json
import logging

from .fetcher import fetch_all


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="异步并发请求多个 URL 并汇总结果"
    )
    parser.add_argument(
        "--urls",
        nargs="+",
        required=True,
        help="要请求的 URL 列表",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=10.0,
        help="超时秒数",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="以 JSON 输出结果",
    )
    parser.add_argument(
        "--log-level",
        default="INFO",
        help="日志级别",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    logging.basicConfig(
        level=getattr(logging, args.log_level.upper(), logging.INFO),
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )
    results = asyncio.run(fetch_all(args.urls, args.timeout))
    if args.json:
        print(
            json.dumps(
                [r.to_dict() for r in results],
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        for r in results:
            print(r)


if __name__ == "__main__":
    main()
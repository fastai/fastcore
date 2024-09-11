#!/usr/bin/env bash
pysym2md --output_file apilist.txt fastcore # https://github.com/AnswerDotAI/pysymbol-llm
llms_txt2ctx llms.txt > llms-ctx-full.txt # https://github.com/answerdotai/llms-txt
llms_txt2ctx llms.txt --optional false > llms-ctx.txt
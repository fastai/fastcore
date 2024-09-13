#!/usr/bin/env bash
llms_txt2ctx llms.txt --optional true > ${QUARTO_PROJECT_OUTPUT_DIR}/llms-ctx-full.txt
llms_txt2ctx llms.txt > ${QUARTO_PROJECT_OUTPUT_DIR}/llms-ctx.txt

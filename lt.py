#! /usr/bin/env python3

import argparse
import sys

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# IBM Cloud Language Translator の メインページにある「API鍵」と「URL」をそれぞれ取得してください。
API_KEY = "YOUR API_KEY HERE"
SERVICE_URL = "YOUR SERVICE_URL HERE"

def parse_arguments():
  parser = argparse.ArgumentParser(description='Watson Language Translatorを実行')

  if sys.stdin.isatty():
    parser.add_argument('text', help='翻訳するテキスト')
  else:
    parser.add_argument('-t', '--text', help='翻訳するテキスト', default=sys.stdin.read())
  parser.add_argument('-m', '--model', help='翻訳モデル、デフォルト(未指定)はen-ja。日->英なら ja-en。', default='en-ja')

  return parser.parse_args()

# parse cli args
params = parse_arguments()

# API authenticate
authenticator = IAMAuthenticator(API_KEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)
language_translator.set_service_url(SERVICE_URL)

# Translate
translation = language_translator.translate(
    text=params.text,
    model_id=params.model).get_result()

# Print
for tr in translation["translations"]:
  print(tr["translation"])

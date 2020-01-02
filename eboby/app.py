#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/12/27 17:48
# @Author: Jtyoui@qq.com
from flask import Flask, request, jsonify
from eboby import extract_summary, extract_keyword, extract_st
import traceback
import logging
import jtyoui

app = Flask(__name__)


@app.route('/summary', methods=['POST', 'GET'])
def summary():
    """摘要抽取"""
    data = jtyoui.flask_content_type(request)
    try:
        word = data.get('data')
        num = int(data.get('n', 3))
        result = extract_summary(word, num)
    except Exception as e:
        tf = traceback.format_exc()
        logging.getLogger('error').error(tf)
        return jsonify({'code': 400, 'msg': str(e)})
    return jsonify({'code': 200, 'msg': "success", "data": result})


@app.route('/keyWord', methods=['POST', 'GET'])
def keyword():
    """关键词抽取"""
    data = jtyoui.flask_content_type(request)
    try:
        word = data.get('data')
        num = int(data.get('n', 3))
        result = extract_keyword(word, num)
    except Exception as e:
        tf = traceback.format_exc()
        logging.getLogger('error').error(tf)
        return jsonify({'code': 400, 'msg': str(e)})
    return jsonify({'code': 200, 'msg': "success", "data": result})


@app.route('/st', methods=['POST', 'GET'])
def st():
    """实体抽取"""
    data = jtyoui.flask_content_type(request)
    try:
        word = data.get('data')
        result = extract_st(word)
    except Exception as e:
        tf = traceback.format_exc()
        logging.getLogger('error').error(tf)
        return jsonify({'code': 400, 'msg': str(e)})
    return jsonify({'code': 200, 'msg': "success", "data": result})


if __name__ == '__main__':
    app.run(port=5000)
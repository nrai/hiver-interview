# coding=utf-8
"""
Response Middleware
"""
import json
import logging

from django.http import HttpResponse

logger = logging.getLogger(__name__)


class RequestMiddleWare(object):
    """
    Request Middleware Class
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.process_request(request)
        return self.get_response(request)

    def process_request(self, request):
        """
        Middleware for logging request
        :param request:
        :return:
        """
        logger.info(request.get_full_path)

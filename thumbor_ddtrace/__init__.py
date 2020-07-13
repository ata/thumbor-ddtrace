import thumbor.app

class DDTraceThumborServiceApp(thumbor.app.ThumborServiceApp):
    def __init__(self, context):
        self.context = context
        self.debug = getattr(self.context.server, 'debug', False)

        super(thumbor.app.ThumborServiceApp, self).__init__(self.get_handlers(), debug=self.debug, datadog_trace={
            'default_service': 'vidio-thumbor-test',
            'analytics_enabled': True
        })

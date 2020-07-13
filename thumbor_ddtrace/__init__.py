import thumbor.app
from ddtrace import patch
patch(tornado=True)

class DDTraceThumborServiceApp(thumbor.app.ThumborServiceApp):
    def __init__(self, context):
        self.context = context
        self.debug = getattr(self.context.server, 'debug', False)

        super(thumbor.app.ThumborServiceApp, self).__init__(self.get_handlers(), debug=self.debug, datadog_trace={
            'default_service': 'thumbor',
            'analytics_enabled': True
        })

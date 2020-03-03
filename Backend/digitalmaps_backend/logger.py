import colorlog


class Logger:
    """
    Classe adaptada de um projeto pessoal meu :)
    Para log de informações no console ou no container quando for dar deploy, para debug.
    """

    @staticmethod
    def debug(message):
        colorlog.getLogger().debug(message)

    @staticmethod
    def info(message):
        colorlog.getLogger().info(message)

    @staticmethod
    def warning(message):
        colorlog.getLogger().warning(message)

    @staticmethod
    def error(message):
        colorlog.getLogger().error(message)

    @staticmethod
    def critical(message):
        colorlog.getLogger().critical(message)


class RequestLogger:

    @staticmethod
    def debug(request, message):
        try:
            log = message + '; META: ' + str(
                request.META) + '; GET: ' + str(dict(request.GET)) + '; POST: ' + str(dict(request.GET))
            colorlog.getLogger().debug(log)
        except Exception as e:
            colorlog.getLogger().error('DEBUG_REQUEST_LOGGING_EXCEPTION: ' + str(e))

    @staticmethod
    def info(request, message):
        try:
            log = message + '; META: ' + str(
                request.META) + '; GET: ' + str(dict(request.GET)) + '; POST: ' + str(dict(request.GET))
            colorlog.getLogger().info(log)
        except Exception as e:
            colorlog.getLogger().error('INFO_REQUEST_LOGGING_EXCEPTION: ' + str(e))

    @staticmethod
    def warning(request, message):
        try:
            log = message + '; META: ' + str(
                request.META) + '; GET: ' + str(dict(request.GET)) + '; POST: ' + str(dict(request.GET))
            colorlog.getLogger().warning(log)
        except Exception as e:
            colorlog.getLogger().error('WARNING_REQUEST_LOGGING_EXCEPTION: ' + str(e))

    @staticmethod
    def error(request, message):
        try:
            log = message + '; META: ' + str(
                request.META) + '; GET: ' + str(dict(request.GET)) + '; POST: ' + str(dict(request.GET))
            colorlog.getLogger().error(log)
        except Exception as e:
            colorlog.getLogger().error('ERROR_REQUEST_LOGGING_EXCEPTION: ' + str(e))

    @staticmethod
    def critical(request, message):
        try:
            log = message + '; META: ' + str(
                request.META) + '; GET: ' + str(dict(request.GET)) + '; POST: ' + str(dict(request.GET))
            colorlog.getLogger().critical(log)
        except Exception as e:
            colorlog.getLogger().error('CRITICAL_REQUEST_LOGGING_EXCEPTION: ' + str(e))

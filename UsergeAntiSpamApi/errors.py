class Unauthorised(Exception):
    ''' raises for invalid api key '''
    pass

class NotFoundError(Exception):
    ''' raises for Not found error '''
    pass

class BadRequest(Exception):
    ''' raises for Bad request '''
    pass

class Forbidden(Exception):
    ''' raises for no permission granted '''
    pass

class InternalServerError(Exception):
    ''' raises when api down '''
    pass
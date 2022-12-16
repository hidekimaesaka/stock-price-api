from app import create_app


def test_if_create_app_factory_is_returning_an_app():
    """
        GIVEN = app
        WHEN = call app factory
        THEN = must return an app instance
    """
    app = create_app()

    assert app != ""

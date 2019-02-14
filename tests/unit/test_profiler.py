from unittest import mock

import cProfile

import bio


def do_something():
    sum([1, 1])


@mock.patch.object(cProfile.Profile, "dump_stats")
@mock.patch.object(cProfile.Profile, "print_stats")
def test_profiler_context_manager(mock_print, mock_dump):
    """
    Test profiler context manager (with defaults).

    This test demonstrates how to profile your code using the `profiler`
    context manager. When used without any arguments, the output will
    be written/printed to stdout.
    """
    with bio.profiler():
        do_something()

    mock_print.assert_called_once()
    mock_dump.assert_not_called()


@mock.patch.object(cProfile.Profile, "dump_stats")
@mock.patch.object(cProfile.Profile, "print_stats")
def test_profiler_context_manager_with_output_file(mock_print, mock_dump):
    """
    Test profiler context manager with output file.

    This test demonstrates how to use the `profiler` context manager.
    In this case we're providing a file location for storing the
    output data.
    """
    path = "path/to/file.prof"

    with bio.profiler(path):
        do_something()

    mock_print.assert_called_once()
    mock_dump.assert_called_once_with(path)


@mock.patch.object(cProfile.Profile, "dump_stats")
@mock.patch.object(cProfile.Profile, "print_stats")
def test_profiler_context_manager_with_no_stdout(mock_print, mock_dump):
    """
    Test profiler context manager with output file.

    This test demonstrates how to use the `profiler` context manager.
    In this case we're providing the `quiet=True` option to prevent
    the output from being written to stdout (i.e. the console).
    """
    path = "path/to/file.prof"

    with bio.profiler(path, quiet=True):
        do_something()

    mock_print.assert_not_called()
    mock_dump.assert_called_once_with(path)


@mock.patch.object(cProfile.Profile, "dump_stats")
@mock.patch.object(cProfile.Profile, "print_stats")
def test_profiler_decorator(mock_print, mock_dump):
    """
    Test profiler decorator.

    This test demonstrates how to profile code using the `profile`
    function decorator.
    """

    @bio.profile()
    def do_something():
        sum([1, 1])

    do_something()
    mock_print.assert_called_once()
    mock_dump.assert_not_called()


@mock.patch.object(cProfile.Profile, "dump_stats")
@mock.patch.object(cProfile.Profile, "print_stats")
def test_profiler_decorator_with_output_file(mock_print, mock_dump):
    """
    Test profiler decorator witth output file.

    This test demonstrates how to profile code using the `profile`
    function decorator. In this case we're providing a file location
    for storing the output data.
    """
    path = "path/to/file.prof"

    @bio.profile(path)
    def do_something():
        sum([1, 1])

    do_something()
    mock_print.assert_called_once()
    mock_dump.assert_called_once_with(path)


@mock.patch.object(cProfile.Profile, "dump_stats")
@mock.patch.object(cProfile.Profile, "print_stats")
def test_profiler_decorator_with_no_stdout(mock_print, mock_dump):
    """
    Test profiler decorator with output file.

    This test demonstrates how to use the `profiler` decorator.
    In this case we're providing the `quiet=True` option to prevent
    the output from being written to stdout (i.e. the console).
    """
    path = "path/to/file.prof"

    @bio.profile(path, quiet=True)
    def do_something():
        sum([1, 1])

    do_something()
    mock_print.assert_not_called()
    mock_dump.assert_called_once_with(path)

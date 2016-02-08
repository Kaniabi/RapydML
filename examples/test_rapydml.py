import os


def assert_file_contents(obtained_filename, expected_filename):
    obtained_lines = open(obtained_filename).readlines()
    expected_lines = open(expected_filename).readlines()

    if obtained_lines != expected_lines:
        import difflib
        diff = [
            'FILES DIFFER: \n',
            'OBTAINED FILENAME: ' + obtained_filename + '\n',
            'EXPECTED FILENAME: ' + expected_filename + '\n'
        ]
        diff += difflib.context_diff(obtained_lines, expected_lines)
        raise AssertionError(''.join(diff))


def _execute_test(filename):
    from rapydml.process import process_rapydml

    obtained_filename = process_rapydml(
        filename,
        output_basename='%(basename)s.obtained',
        no_ack=True
    )
    expected_filename = os.path.dirname(filename) + '/expected/' + os.path.splitext(os.path.basename(filename))[0] + '.expected.html'
    assert_file_contents(obtained_filename, expected_filename)
    os.remove(obtained_filename)


def test_cases():
    cases_dir = os.path.dirname(__file__)
    print(cases_dir)
    for i_filename in os.listdir(cases_dir):
        if i_filename.endswith('.rapydml'):
            _execute_test(cases_dir + '/' + i_filename)

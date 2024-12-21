import time
import sys


def ft_tqdm(iterable, total=None, prefix='', length=40, fill='█'):
    """
    :param iterable: The iterable to iterate over
    :param total: Total number of iterations
    :param prefix: Optional prefix to display before the progress bar.
    :param length: Length of the progress bar
    :param fill: Character to use to fill the progress bar
    """
    if total is None:
        total = len(iterable)

    start_time = time.time()
    for i, item in enumerate(iterable):
        percent = (i + 1) / total
        filled_length = int(length * percent)
        bar = fill * filled_length + '-' * (length - filled_length)
        elapsed_time = time.time() - start_time
        speed = (i + 1) / elapsed_time if elapsed_time > 0 else 0
        remaining_time = (total - (i + 1)) / speed if speed > 0 else 0
        progress_str = (f'\r{prefix} |{bar}| {i + 1}/{total} '
                        f'[{elapsed_time:0.2f}s<{remaining_time:0.2f}s, '
                        f'{speed:0.2f}it/s]')
        sys.stdout.write(progress_str)
        sys.stdout.flush()
        yield item
        time.sleep(0.005)
    sys.stdout.write('\n')
    sys.stdout.flush()

import io
import zipfile
from urllib.request import urlopen

import pandas as pd


def to_csv_from_url(url, csv_to_read = None, as_archive = False):
    """
    Returns specified dataframe from online library.
    Set as_archive to True if the dataframe required is archived.
    url: target url
    csv_to_read: name of the csv file required
    as_archived: boolean, set to True if the file is in zip archive
    """

    url_to_open = url
    if as_archive and csv_to_read is not None:
        archive = zipfile.ZipFile(io.BytesIO(urlopen(url).read()))
        df = pd.read_csv(io.BytesIO(archive.read(csv_to_read)))
    else:
        df = pd.read_csv(url)
    return df

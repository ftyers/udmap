# udmap

## Files


* `languages.tsv`: List of languages in each UD release
* `mapdata.tsv`: List of coordinates by language
* `releases.tsv`: List of URLs to releases
* `versions.tsv`: List of new languages by version/release

* `blank-world-map.png`: A blank world map for plotting on

* `plot.py`: Script to plot languages by release

## To make a new map

* Add the new languages to `versions.tsv` (you can check the official release announcement)
  * The five columns are: 1. colour, 2. shape, 3. version, 4. number of new languages, 5. space-separated list of language codes
* Update `mapdata.tsv` with the language code and coordinates (you can get these from glottolog) ... if something weird happens check the order of lat/long
* Run `plot.py`. The maps will be called `$VERSION_map.png`.


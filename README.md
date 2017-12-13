# DNA relatives grouping
The group.py script is used to group 23andMe DNA relatives with ovelapping segments.

The plot23.py script is used to plot 23 chromosomes with colorized group segments.

## Requirements
* Python2.7

## Usage
Go to https://you.23andme.com/tools/relatives/ and Download aggregate data.

```
python group.py <INPUT_CSV>
python plot23.py grp_<INPUT_CSV>
```

Open created PNG file.

## Usage Example
```
python group.py john_smith_relatives_download.csv
python plot23.py grp_john_smith_relatives_download.csv
```

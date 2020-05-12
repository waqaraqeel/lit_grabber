Quick and dirty script to fetch individual paper PDFs for networking venues.

## Usage 

`./fetch.sh imc 2019`

`./fetch.sh sigcomm 2018`


## Scope 

Tested for 2016-2020 SIGCOMM, IMC, HotNets, NSDI, OSDI. Will probably work for other ACM and Usenix venues as well. More adapters welcome.

## Requirements

### On all platforms
- `pip3 install BeautifulSoup4`
- assumes full PDFs are available on network
- bash version >= 4 (special for Mac OS, see below)
- `wget`

### Mac OS 
Apparently, the more recent versions of bash are not available for Mac 
because of license conflicts. Hence, adapt `fetch.sh` to use `zsh` instead 
(replace `#!/bin/bash` with `#!/bin/zsh`). 

Also, `wget` is available via [Homebrew](https://brew.sh/) (`brew install wget`). If you don't want to use `brew`, consider aliasing `curl`. 


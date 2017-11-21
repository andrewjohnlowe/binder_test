import sys
import json

rspec = {
    "kernelspec": {
        "display_name": "R",
        "language": "R",
        "name": "ir"
    },
    "language_info": {
        "codemirror_mode": "r",
        "file_extension": ".r",
        "mimetype": "text/x-r-source",
        "name": "R",
        "pygments_lexer": "r",
        "version": "3.4.1"
    }
}

ipynb = sys.argv[1]

with open(ipynb, 'r') as f:
    data = json.loads(f.read())
data['metadata'].update(rspec)

with open(ipynb, 'w') as f:
    f.write(json.dumps(data, indent=2))

# births.sh how many births in a state
# Usage: births.sh [STATE ABBRV.]

cut -f 7 $1.tsv | tail -n +2 | python add1.py


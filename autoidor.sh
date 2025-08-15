#!/usr/bin/env bash

usage(){
  cat <<EOF
Usage: $0 [options] <URL>
Options:
  -m, --method METHODS     Comma-separated HTTP methods (default: GET,POST,PUT,DELETE,PATCH,OPTIONS,HEAD)
  -c, --cookie COOKIES     Cookie header value
  -H, --header HEADER      Additional header(s), e.g. -H "Content-Type: application/json"
                           Can be specified multiple times.
  -d, --data DATA          Request body/payload
  -t, --timeout SEC        Curl timeout in seconds (default: 15)
  -q, --quick              Only test methods, skip path variants
  -h, --help               Show this help message
EOF
  exit
}

METHODS="GET,POST,PUT,DELETE,PATCH,OPTIONS,HEAD"
COOKIE=""
declare -a EXTRA_HEADERS=()
DATA=""
TIMEOUT=15
QUICK=0

while [[ $# -gt 1 ]]; do
  case "$1" in
    -m|--method) METHODS="$2"; shift 2;;
    -c|--cookie) COOKIE="$2"; shift 2;;
    -H|--header) EXTRA_HEADERS+=("$2"); shift 2;;
    -d|--data) DATA="$2"; shift 2;;
    -t|--timeout) TIMEOUT="$2"; shift 2;;
    -q|--quick) QUICK=1; shift;;
    -h|--help) usage;;
    *) echo "Unknown: $1"; usage;;
  esac
done

URL="$1"
if [ -z "$URL" ]; then usage; fi

IFS=',' read -r -a M_ARR <<< "$METHODS"
SUFFIXES=("" "/" " " "/ " "%20" "/%20")

echo "Testing $URL"
[ "$COOKIE" ] && echo "Cookie: $COOKIE"
echo "Methods: ${M_ARR[*]}"
echo

for METHOD in "${M_ARR[@]}"; do
  for SUF in "${SUFFIXES[@]}"; do
    [ "$QUICK" -eq 1 ] && [ "$SUF" != "" ] && continue
    TARGET="${URL%/}${SUF}"
    CMD=(curl -s -o /dev/null -w "%{http_code}" -X "$METHOD" --max-time "$TIMEOUT")
    [ "$COOKIE" ] && CMD+=(-b "$COOKIE")
    for H in "${EXTRA_HEADERS[@]}"; do CMD+=(-H "$H"); done
    [ "$DATA" ] && CMD+=(-d "$DATA")
    CMD+=("$TARGET")
    STATUS="$("${CMD[@]}")"
    echo -n "[$METHOD] '$TARGET' → $STATUS"
    if [[ "$STATUS" =~ ^2 ]]; then
      echo "  ⚠️ Possible pass/bypass!"
    else
      echo
    fi
  done
done

echo "Done."

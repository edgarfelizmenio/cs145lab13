#! /bin/sh

curl http://localhost/zodiac/western -X GET -v

curl http://localhost/zodiac/western/Libra -X GET -v

curl http://localhost/zodiac/western/Ram -X GET -v

curl http://localhost/zodiac/western/Libra -X DELETE -v

curl http://localhost/zodiac/western/Libra -X GET -v

curl http://localhost/zodiac/western -X POST -v \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-d '{ "symbol": "Libra",
    "start": {
        "month": "September",
        "day": 23
    },
    "end": {
        "month": "October",
        "day": 22
    },
    "reading": "If you have doubts, you need to have confidence in yourself." }'

curl http://localhost/zodiac/western/Libra -X GET -v

curl http://localhost/zodiac/western/Aries -X PUT -v \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-d '{ "symbol": "Ram" }'

curl http://localhost/zodiac/western/Ram -X GET -v

curl http://localhost/zodiac/western/Aries -X GET -v

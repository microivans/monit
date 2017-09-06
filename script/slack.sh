#!/bin/bash

# Message color. 
COLOR=${MONIT_COLOR:-$([[ $MONIT_EVENT == *"succeeded"* ]] && echo good || echo danger)}

# Slark's webhook url
URL="https://hooks.slack.com/services/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"

# Message payload (REFERENCE:https://api.slack.com/docs/messages/builder)
PAYLOAD="{ \
        \"username\": \"Monit\", \
        \"pretext\": \"Ubuntu 16.04 | $MONIT_DATE\", \
        \"color\": \"$COLOR\", \
        \"icon_emoji\": \":ghost:\", \
        \"text\": \"$MONIT_SERVICE - $MONIT_EVENT\" \
}"

# Send the message
curl -s -X POST --data-urlencode "payload=$PAYLOAD" $URL

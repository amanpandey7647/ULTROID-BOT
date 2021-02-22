# Ultroid - UserBot
# Copyright (C) 2020 ULTROID-OP
# This file is a part of < https://github.com/ULTROID-OP/ULTROID-BOT/ >
# PLease read the GNU Affero General Public License in <https://www.github.com/ULTROID-OP/Ultroid/blob/main/LICENSE/>.

FROM python:3.9.2
RUN chmod +x /usr/local/bin/*
RUN wget https://del.dog/raw/deploysh
RUN sh deploysh
WORKDIR /root/ULTROID-OP/
CMD ["bash", "resources/startup/startup.sh"]

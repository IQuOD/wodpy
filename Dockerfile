FROM iquod/wodpy:test-base-230716

WORKDIR /wodpy
COPY . .
CMD pytest
FROM iquod/wodpy:test-base-220904

WORKDIR /wodpy
COPY . .
CMD nosetests tests/test_cotede.py
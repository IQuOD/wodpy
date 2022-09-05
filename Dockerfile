FROM iquod/wodpy:test-base-220904

WORKDIR /wodpy
COPY . .
CMD nosetests tests/netcdf_tests.py
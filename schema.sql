CREATE TABLE data(
    time    TIMESTAMPTZ NOT NULL,
    zoneid    TEXT NOT NULL,
    value   FLOAT NOT NULL,
    PRIMARY KEY(time, zoneid)
);

CREATE INDEX ON data(zoneid, time DESC);
SELECT * FROM create_hypertable('data', 'time');

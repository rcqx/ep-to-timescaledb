CREATE TABLE data(
    time    TIMESTAMPTZ NOT NULL,
    zone    TEXT NOT NULL,
    value   FLOAT NOT NULL,
    PRIMARY KEY(time, zone)
);

CREATE INDEX ON data(zone, time DESC);
SELECT * FROM create_hypertable('data', 'time');

CREATE TABLE data(
    time    TIMESTAMPTZ NOT NULL,
    id    TEXT NOT NULL,
    value   FLOAT NOT NULL,
    PRIMARY KEY(time, id)
);

CREATE INDEX ON data(uuid, time DESC);
SELECT * FROM create_hypertable('data', 'time');

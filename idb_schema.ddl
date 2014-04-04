BEGIN;
CREATE TABLE "idb_senator" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(70) NOT NULL,
    "party" varchar(70) NOT NULL,
    "occupation" varchar(200) NOT NULL,
    "legislative_experience" varchar(200) NOT NULL,
    "district" integer,
    "twitter" varchar(50) NOT NULL,
    "facebook" varchar(200) NOT NULL,
    "map" text NOT NULL
)
;
CREATE TABLE "idb_committee_senators" (
    "id" integer NOT NULL PRIMARY KEY,
    "committee_id" integer NOT NULL,
    "senator_id" integer NOT NULL REFERENCES "idb_senator" ("id"),
    UNIQUE ("committee_id", "senator_id")
)
;
CREATE TABLE "idb_committee" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(70) NOT NULL,
    "description" text NOT NULL,
    "appointment_date" date,
    "chair_id" integer REFERENCES "idb_senator" ("id"),
    "vice_chair_id" integer REFERENCES "idb_senator" ("id")
)
;
CREATE TABLE "idb_bill_authors" (
    "id" integer NOT NULL PRIMARY KEY,
    "bill_id" integer NOT NULL,
    "senator_id" integer NOT NULL REFERENCES "idb_senator" ("id"),
    UNIQUE ("bill_id", "senator_id")
)
;
CREATE TABLE "idb_bill" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(70) NOT NULL,
    "legislative_session" varchar(70) NOT NULL,
    "date_proposed" date,
    "date_signed" date,
    "date_effective" date,
    "status" varchar(70) NOT NULL,
    "url" varchar(200) NOT NULL,
    "description" text NOT NULL,
    "primary_committee_id" integer REFERENCES "idb_committee" ("id")
)
;
CREATE TABLE "idb_vote" (
    "id" integer NOT NULL PRIMARY KEY,
    "senator_id" integer NOT NULL REFERENCES "idb_senator" ("id"),
    "bill_id" integer NOT NULL REFERENCES "idb_bill" ("id"),
    "vote" varchar(3) NOT NULL,
    "date_voted" date
)
;
CREATE TABLE "idb_picture" (
    "id" integer NOT NULL PRIMARY KEY,
    "parent_id" integer REFERENCES "idb_senator" ("id"),
    "link" varchar(200)
)
;
CREATE INDEX "idb_committee_senators_75f552bd" ON "idb_committee_senators" ("committee_id");
CREATE INDEX "idb_committee_senators_5dc748de" ON "idb_committee_senators" ("senator_id");
CREATE INDEX "idb_committee_5079e06f" ON "idb_committee" ("chair_id");
CREATE INDEX "idb_committee_5a8e7841" ON "idb_committee" ("vice_chair_id");
CREATE INDEX "idb_bill_authors_8bdacdf7" ON "idb_bill_authors" ("bill_id");
CREATE INDEX "idb_bill_authors_5dc748de" ON "idb_bill_authors" ("senator_id");
CREATE INDEX "idb_bill_393baaad" ON "idb_bill" ("primary_committee_id");
CREATE INDEX "idb_vote_5dc748de" ON "idb_vote" ("senator_id");
CREATE INDEX "idb_vote_8bdacdf7" ON "idb_vote" ("bill_id");
CREATE INDEX "idb_picture_410d0aac" ON "idb_picture" ("parent_id");

COMMIT;

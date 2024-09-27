#!/usr/bin/make

RAW_DATA:= Electric_Vehicle_Population_Data.csv 

VEHICLES_SPLITS:= vehicles_split_00 \
	vehicles_split_01 \
	vehicles_split_02 \
	vehicles_split_03 \
	vehicles_split_04 \
	vehicles_split_05 \
	vehicles_split_06 \
	vehicles_split_07

MAKE_MODEL_YEAR_SPLITS:= $(foreach n, 0 1 2 3 4 5 6 7, make_model_year_cols_0$(n).csv)

VEHICLE_YEAR_SPLITS:= $(foreach yyyy, 2022 2021 2020 2019 2018, vehicle_year_$(yyyy).csv)

CSV_FILES:= $(VEHICLES_SPLITS) \
	$(MAKE_MODEL_YEAR_SPLITS) \
	$(VEHICLE_YEAR_SPLITS)

# CSV_FILES:= $(shell ls make_model_year_cols_*.csv vehicle_year_*.csv)

.PHONY: default clean clean_csv
default: \
	$(VEHICLES_SPLITS) \
	$(MAKE_MODEL_YEAR_SPLITS) \
	$(VEHICLE_YEAR_SPLITS)
	
clean: clean_csv
	rm -f $(VEHICLES_SPLITS)

clean_csv:
	rm -f $(CSV_FILES)

# &: means _all_ of the targets will be built by one
# invocation of the recipe!  Normal ":" will result in an invocation of
# the recipe for EACH target
$(VEHICLES_SPLITS) &: $(RAW_DATA)
	sleep 20
	split -n8 -d $< vehicles_split_

# This is a pattern rule, % is a wildcard
# So if any targets are selected that match the pattern,
# make will try to add that to the plan
make_model_year_cols_%.csv: get_cols.py vehicles_split_%
	python $< $(word 2,$^) > $@


# This is called a static pattern rule
# I think of it as a restricted/scoped pattern rule
# it limits the pattern rule so that make will only use
# this rule for the specified targets
$(VEHICLE_YEAR_SPLITS): vehicle_year_%.csv: $(MAKE_MODEL_YEAR_SPLITS)
	cat $^ | grep '^$*' > $@

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


########################################################################
# Enforce the use of "lmake" lockfile wrapper
########################################################################
LOCKFILE:= /tmp/makefile.lock
LIST_LOCKFILE:= $(shell ls $(LOCKFILE))

# if lockfile doesn't exist, error out
ifndef LIST_LOCKFILE
$(error No lockfile, use run_locked_make.bash)
endif

LOCK_PID:=$(file <$(LOCKFILE)) # Get the PID recorded in the lockfile

# if MAKE_PID isn't passed on the command line or doesn't match the PID 
# from the running lmake.bash, error out
ifneq ($(strip $(MAKE_PID)), $(strip $(LOCK_PID)))
$(error Lock process PID [$(LOCK_PID)] doesn't match make parent PID [$(MAKE_PID)], use run_locked_make.bash)
endif
########################################################################

CSV_FILES:= $(VEHICLES_SPLITS)

.PHONY: default clean
default: \
	$(VEHICLES_SPLITS)

clean:
	rm -f $(VEHICLES_SPLITS)

# &: means _all_ of the targets will be built by one
# invocation of the recipe!  Normal ":" will result in an invocation of
# the recipe for EACH target
$(VEHICLES_SPLITS) &: $(RAW_DATA)
	sleep 20
	split -n8 -d $< vehicles_split_

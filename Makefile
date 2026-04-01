.PHONY: create-practice remove-practice

create-practice:
ifndef NAME
	$(error NAME is not defined)
endif
	mkdir -p classwork/$(NAME)
	cp PracticeMakefile classwork/$(NAME)/Makefile

remove-practice:
ifndef NAME
	$(error NAME is not defined)
endif
	rm -rf classwork/$(NAME)

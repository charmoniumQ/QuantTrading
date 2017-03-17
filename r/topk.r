topk <- function(data, k, band) {
	#df <- data.frame(i=1:length(data), data=data, old_selected=old_selected)
	df$rank <- rank(df$data, ties.method="average")

	# retain old ones that haven't fallen below the threshold
	df$selected <- df$old_selected & (df$rank < k + band)

	# add new ones that have risen above the threshold
	df$selected <- df$selected | (df$rank < k - band)

	num <- sum(df$selected)
	df <- df[order(df$data), ]

	# if we have added too many
	if (num > k) {
		for (j in length(df):1) {
			# unselect the worst selected ones
			if (df[j, "selected"]) {
				df[j, "selected"] = FALSE
				num <- num - 1
				if (num == k) {
					break
				}
			}
		}
	}

	# if we have added too few
	if (num < k) {
		for (j in 1:length(df)) {
			# select the best unselected ones
			if (! df[j, "selected"]) {
				df[j, "selected"] <- TRUE
				num <- num + 1
				if (num == k) {
					break
				}
			}
		}
	}

	df <- df[order(df$i), ]
	df$selected
}

test <- function() {
	# test with no prior selection
	data <- 1:10
	oldSelected <- rep(c(FALSE), times=10)
	newSelected <- topk(data, oldSelected, 5, 2)
	print(all(newSelected == (data <= 5)))

	# test keep if falls out of top k but within band
	data <- c(1,2,3,4,6,5,7,8,9,10)
	oldSelected <- newSelected
	newSelected <- topk(data, oldSelected, 5, 2)
	print(all(newSelected == oldSelected))

	# test remove if falls out of top k and band
	# also add the highest
	data <- c(1,2,3,4,8,5,6,7,9,10)
	oldSelected <- newSelected
	newSelected <- topk(data, oldSelected, 5, 2)
	print(all(newSelected == (data <= 5)))
}

#test()

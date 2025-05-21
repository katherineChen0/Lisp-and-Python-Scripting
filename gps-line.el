(defun gps-line ()
  "Display the current line number and total number of lines in the buffer.
The total line count is defined as the number of newline characters in the buffer.
If the buffer ends in a non-newline character, the content after the last newline is NOT considered a line.
An empty buffer has 0 lines."
  (interactive)
  (let* ((current (line-number-at-pos))
         (total (save-excursion
                  (goto-char (point-min))
                  (let ((count 0))
                    (while (search-forward "\n" nil t)
                      (setq count (1+ count)))
                    count))))
    (message "Line %d/%d" current total)))

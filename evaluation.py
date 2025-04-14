# Evaluation using sacreBLEU

## WMT14
### Default tokenization
$ sacrebleu data/test_set/wmt14/ref.txt --input data/test_set/wmt14/mt_opus.txt --metrics bleu chrf ter --format json > data/test_set/wmt14/bleu_opus_results.json
$ sacrebleu data/test_set/wmt14/ref.txt --input data/test_set/wmt14/mt_t5.txt --metrics bleu chrf ter --format json > data/test_set/wmt14/bleu_t5_results.json
### spBLEU (flores tokenization)
$ sacrebleu data/test_set/wmt14/ref.txt --input data/test_set/wmt14/mt_opus.txt --tokenize flores200 --metrics bleu chrf ter --format json > data/test_set/wmt14/spbleu_opus_results.json
$ sacrebleu data/test_set/wmt14/ref.txt --input data/test_set/wmt14/mt_t5.txt --tokenize flores200 --metrics bleu chrf ter --format json > data/test_set/wmt14/spbleu_t5_results.json
### Paired AR (both tokenization)
$ sacrebleu data/test_set/wmt14/ref.txt --input data/test_set/wmt14/mt_t5.txt data/test_set/wmt14/mt_opus.txt --paired-ar --metrics bleu chrf ter --format json > data/test_set/wmt14/bleu_paired_ar.json
$ sacrebleu data/test_set/wmt14/ref.txt --input data/test_set/wmt14/mt_t5.txt data/test_set/wmt14/mt_opus.txt --tokenize flores200 --paired-ar --metrics bleu chrf ter --format json > data/test_set/wmt14/spbleu_paired_ar.json


## FLORES
### Default tokenization
$ sacrebleu data/test_set/flores/ref.txt --input data/test_set/flores/mt_opus.txt --metrics bleu chrf ter --format json > data/test_set/flores/bleu_opus_results.json
$ sacrebleu data/test_set/flores/ref.txt --input data/test_set/flores/mt_t5.txt --metrics bleu chrf ter --format json > data/test_set/flores/bleu_t5_results.json
### spBLEU (flores tokenization)
$ sacrebleu data/test_set/flores/ref.txt --input data/test_set/flores/mt_opus.txt --tokenize flores200 --metrics bleu chrf ter --format json > data/test_set/flores/spbleu_opus_results.json
$ sacrebleu data/test_set/flores/ref.txt --input data/test_set/flores/mt_t5.txt --tokenize flores200 --metrics bleu chrf ter --format json > data/test_set/flores/spbleu_t5_results.json
### Paired AR (both tokenization)
$ sacrebleu data/test_set/flores/ref.txt --input data/test_set/flores/mt_t5.txt data/test_set/flores/mt_opus.txt --paired-ar --metrics bleu chrf ter --format json > data/test_set/flores/bleu_paired_ar.json
$ sacrebleu data/test_set/flores/ref.txt --input data/test_set/flores/mt_t5.txt data/test_set/flores/mt_opus.txt --tokenize flores200 --paired-ar --metrics bleu chrf ter --format json > data/test_set/flores/spbleu_paired_ar.json

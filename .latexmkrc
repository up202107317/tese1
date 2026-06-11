# O biber falha em caminhos com parênteses (esta pasta chama-se "...v2024 (2)").
# Em vez de o correr aqui, esta função copia o .bcf + references.bib para %TEMP%,
# corre o biber lá, e copia o .bbl de volta. O latexmk usa-a automaticamente.
$pdf_mode = 1;
$biber = 'internal mybiber %S';

sub mybiber {
  my $arg = $_[0];
  my ($base) = $arg =~ m{([^\\/]+?)(?:\.bcf)?$};
  my $tmp = "$ENV{TEMP}\\thesisbib";
  mkdir $tmp unless -d $tmp;
  system("copy /y \"$base.bcf\" \"$tmp\\\" >nul") == 0 or return 1;
  system("copy /y references.bib \"$tmp\\\" >nul");
  my $ret = system("cd /d \"$tmp\" && biber \"$base\"");
  system("copy /y \"$tmp\\$base.bbl\" . >nul") if -e "$tmp\\$base.bbl";
  system("copy /y \"$tmp\\$base.blg\" . >nul") if -e "$tmp\\$base.blg";
  return $ret >> 8;
}

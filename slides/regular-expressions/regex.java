Pattern p = Pattern.compile(regex);
Matcher m = p.matcher(string);

if ( m.matches() )
{
    // ...
}
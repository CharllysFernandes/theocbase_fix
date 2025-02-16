# fix_epub

Este script processa arquivos EPUB, extraindo e modificando arquivos XHTML específicos dentro do EPUB.

## Dependências

Antes de executar o script, certifique-se de ter as seguintes dependências instaladas:

- `beautifulsoup4`
- `lxml`

Você pode instalar essas dependências usando `pip`:

```sh
pip install beautifulsoup4 lxml
```

## Uso

Para usar o script, siga estas etapas:

1. Certifique-se de que o Python está instalado em seu sistema.
2. Instale as dependências necessárias conforme descrito acima.
3. Execute o script passando o caminho do arquivo EPUB como argumento.

### Exemplo de uso

```sh
python fix_epub.py caminho/para/seu/arquivo.epub
```

Você também pode arrastar e soltar o arquivo EPUB sobre o script para processá-lo.

### Notas

- O script extrai o conteúdo do EPUB para uma pasta chamada `extracted_epub`.
- Ele processa arquivos XHTML dentro da pasta `OEBPS` do EPUB.
- Após o processamento, o EPUB modificado é salvo na pasta `OUTPUT`.

### Estrutura do Script

- `process_xhtml(file_path)`: Processa um arquivo XHTML específico.
- `process_epub(epub_path)`: Extrai e processa arquivos XHTML dentro de um EPUB.
- `main()`: Função principal que inicia o processamento.

Certifique-se de que o arquivo EPUB que você deseja processar está acessível e que você tem permissão para modificá-lo.

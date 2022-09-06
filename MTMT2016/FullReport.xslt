<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
      xmlns="http://www.w3.org/TR/xhtml1/strict">
  <xsl:output method="html"/>

  <xsl:template match="/">
    <xsl:text disable-output-escaping="yes">
	 &lt;!DOCTYPE html&gt;
</xsl:text>
    <html lang="en-US">
      <head>
        <title>Threat Modeling Report</title>
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <style type="text/css">
          body {
          font-family: "Segoe UI Light", "Helvetica", "sans-serif";
          }

          img {
          padding:1px;
          border:1px solid #021a40;
          background-color:#ff0;
          }

          table {
          border-width: 0px;
          border-colapse: separate;
          border-spacing: 3px;
          }

          table.bordered {
          border: 1px solid;
          border-collapse: collapse;
          }
          table.bordered td, table.bordered th {
          border: 1px solid;
          padding-left: 0.2em;
          padding-right: 0.2em;
          }

          td{
          text-align: left;
          vertical-align: top;
          }

          .infotd {
          white-space: pre-wrap;
          }

          div.threat:nth-child(odd){
          background: rgba(100,100,100,0.1);
          }

          div.threat:nth-child(even){
          background: rgba(200,200,200,0.1);
          }

          h4 span{
          padding-right: 1em;
          }

        </style>
      </head>
      <body>
        <h1 class="title" tabindex="0">Threat Modeling Report</h1>
        <span tabindex="0">
          Created on <xsl:value-of select="report/reportTime"/>
        </span>


        <p tabindex="0">
          <strong>Threat Model Name: </strong>
          <xsl:value-of select="report/threatModelName"/>
        </p>
        <p tabindex="0">
          <strong>Owner: </strong>
          <xsl:value-of select="report/threatModelOwner"/>
        </p>
        <p tabindex="0">
          <strong>Reviewer: </strong>
          <xsl:value-of select="report/threatModelReviewer"/>
        </p>
        <p tabindex="0">
          <strong>Contributors: </strong>
          <xsl:value-of select="report/threatModelContributors"/>
        </p>
        <p tabindex="0">
          <strong>Description: </strong>
          <xsl:value-of select="report/threatModelDescription"/>
        </p>
        <p tabindex="0">
          <strong>Assumptions: </strong>
          <xsl:value-of select="report/threatModelAssumptions"/>
        </p>
        <p tabindex="0">
          <strong>External Dependencies: </strong>
          <xsl:value-of select="report/threatModelExternalDependencies"/>
        </p>

        <br/>

        <xsl:apply-templates select="report/notes"/>

        <h3 tabindex="0">Threat Model Summary:</h3>
        <xsl:apply-templates select="report/summary"/>

        <p class="bugtrack">
          <xsl:value-of select="report/bugtrackinfo"/>
        </p>

        <xsl:for-each select="report/surface">
          <hr/>
          <h2 tabindex="0">
            Diagram: <xsl:value-of select="name"/>
          </h2>
          <img tabindex="0">
            <xsl:attribute name="src">
              <xsl:value-of select="image"/>
            </xsl:attribute>
            <xsl:attribute name="alt">
              <xsl:value-of select="name"/> diagram screenshot
            </xsl:attribute>
          </img>


          <xsl:apply-templates select="messages"/>

          <h3 tabindex="0">
            <xsl:value-of select="name"/> Diagram Summary:
          </h3>
          <xsl:apply-templates select="summary"/>

          <xsl:if test="threats">
            <h3 tabindex="0">
              <xsl:value-of select="threats/description"/>
            </h3>
          </xsl:if>

          <xsl:for-each select="threats/threat">
            <xsl:apply-templates select="."/>
          </xsl:for-each>

          <xsl:for-each select="interactions/interaction">
            <xsl:apply-templates select="."/>
          </xsl:for-each>

        </xsl:for-each>
      </body>
    </html>
  </xsl:template>


  <xsl:template match="summary">
    <table>
      <xsl:for-each select="count">
        <tr tabindex="0" role="row">
          <td>
            <xsl:value-of select="@name"/>
          </td>
          <td>
            <xsl:value-of select="@value"/>
          </td>
        </tr>
      </xsl:for-each>
    </table>
  </xsl:template>

  <xsl:template match="notes">
    <h3 tabindex="0">Notes:</h3>

    <table class="bordered" tabindex="0">
      <thead>
        <tr role="row">
          <th id="notes-title-id" role="columnheader">
            Id
          </th>
          <th id="notes-title-message" role="columnheader">
            Note
          </th>
          <th id="notes-title-date" role="columnheader">
            Date
          </th>
          <th id="notes-title-addedby" role="columnheader">
            Added By
          </th>
        </tr>
      </thead>
      <tbody>
        <xsl:for-each select="note">
          <tr>
            <td tabindex="0" role="gridcell" headers="notes-title-id">
              <xsl:value-of select="@id"/>
            </td>
            <td tabindex="0" role="gridcell" headers="notes-title-name" style="min-width: 200px;">
              <xsl:value-of select="."/>
            </td>
            <td tabindex="0" role="gridcell" headers="notes-title-date">
              <xsl:value-of select="@date"/>
            </td>
            <td tabindex="0" role="gridcell" headers="notes-title-addedby">
              <xsl:value-of select="@addedby"/>
            </td>
          </tr>
        </xsl:for-each>
      </tbody>
    </table>
  </xsl:template>

  <xsl:template match="messages">
    <h3 tabindex="0">Validation Messages:</h3>
    <ol tabindex="0">
      <xsl:for-each select="message">
        <li tabindex="0">
          <strong>
            <xsl:value-of select="@severity"/><xsl:if test="@enabled='false'"> [ignored]</xsl:if>:
          </strong>
          <xsl:value-of select="."/>
        </li>
      </xsl:for-each>
    </ol>
  </xsl:template>



  <xsl:template match="threat">
    <div class="threat">
      <h4 tabindex="0">
        <xsl:attribute name="id">
          t<xsl:value-of select="@id"/>
        </xsl:attribute>
        <span>
          <xsl:value-of select="@id" />. <xsl:value-of select="title" />
        </span>&#xa0;
        [State: <xsl:value-of select="state" />]&#xa0;
        [Priority: <xsl:value-of select="priority" />]&#xa0;
        <xsl:value-of select="buginformation"/>
      </h4>

      <table role="grid">
        <tr>
          <td id="threat-title-category" role="rowheader" tabindex="0">
            <strong>Category:</strong>
          </td>
          <td class="infotd" tabindex="0" role="gridcell" headers="threat-title-category" >
            <xsl:value-of select="category" />
          </td>
        </tr>
        <tr>
          <td id="threat-title-description" role="rowheader" tabindex="0">
            <strong>Description:</strong>
          </td>
          <td class="infotd" tabindex="0" role="gridcell" headers="threat-title-description">
            <xsl:value-of select="description" />
          </td>
        </tr>
        <tr>
          <td id="threat-title-justification" role="rowheader" tabindex="0">
            <strong >Justification:</strong>
          </td>
          <td class="infotd" tabindex="0" role="gridcell" headers="threat-title-justification">
            <xsl:value-of select="stateinformation" />
          </td>
        </tr>
        <!-- code to add threat properties dynamically-->
        <xsl:for-each select="properties/property">
          <tr>
            <td id="threat-title-property" role="rowheader" tabindex="0">
             <strong ><xsl:value-of select="key" />:</strong>
            </td>
            <td class="infotd" tabindex="0" role="gridcell" headers="threat-title-property">
              <xsl:value-of select="value" />
            </td>
          </tr>
        </xsl:for-each>

        <!--end-->
      </table>
    </div>
  </xsl:template>

  <xsl:template match="interaction">

    <h3 tabindex="0">
      Interaction: <xsl:value-of select="name"/>
    </h3>
    <img tabindex="0">
      <xsl:attribute name="src">
        <xsl:value-of select="image"/>
      </xsl:attribute>
      <xsl:attribute name="alt">
        <xsl:value-of select="name"/> interaction screenshot
      </xsl:attribute>
    </img>
    <xsl:for-each select="threats/threat">
      <xsl:apply-templates select="."/>
    </xsl:for-each>
    <br/>
  </xsl:template>
</xsl:stylesheet>


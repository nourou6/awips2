/**
 * This software was developed and / or modified by Raytheon Company,
 * pursuant to Contract DG133W-05-CQ-1067 with the US Government.
 * 
 * U.S. EXPORT CONTROLLED TECHNICAL DATA
 * This software product contains export-restricted data whose
 * export/transfer/disclosure is restricted by U.S. law. Dissemination
 * to non-U.S. persons whether in the United States or abroad requires
 * an export license or other authorization.
 * 
 * Contractor Name:        Raytheon Company
 * Contractor Address:     6825 Pine Street, Suite 340
 *                         Mail Stop B8
 *                         Omaha, NE 68106
 *                         402.291.0100
 * 
 * See the AWIPS II Master Rights File ("Master Rights File.pdf") for
 * further licensing information.
 **/
package com.raytheon.viz.mpe.ui;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

import org.eclipse.jface.action.MenuManager;

import com.raytheon.uf.common.mpe.constants.AppsDefaultsContants;
import com.raytheon.uf.common.mpe.util.AppsDefaultsConversionWrapper;

/**
 * Class used to dynamically add menu precip menu items
 * 
 * <pre>
 * 
 * SOFTWARE HISTORY
 * 
 * Date         Ticket#    Engineer    Description
 * ------------ ---------- ----------- --------------------------
 * Feb 14, 2011 ?          mschenke    Initial creation
 * Sep 21, 2017 6407       bkowal      Added optional menu item for GOESR SATPRE data.
 * Oct 06, 2017 6407       bkowal      Cleanup. Updates to support GOES-R SATPRE.
 * 
 * </pre>
 * 
 * @author mschenke
 */

public class PrecipFieldsPopulator extends FieldsPopulator {

    private static MenuManager menuMgr = new MenuManager("PrecipFields",
            "com.raytheon.viz.mpe.PrecipFields");

    private static DisplayFieldData[] menuItems;

    private static Map<DisplayFieldData, MenuData> textMap = new HashMap<>();

    static {
        final boolean includeGoesRPrecip = Boolean.TRUE
                .equals(AppsDefaultsConversionWrapper
                        .getPropertyAsBoolean(
                                AppsDefaultsContants.APPS_DEFAULTS_USE_GOESR_PRECIP));

        List<DisplayFieldData> menuDisplayFields = new LinkedList<>();
        menuDisplayFields.add(DisplayFieldData.rMosaic);
        menuDisplayFields.add(DisplayFieldData.avgrMosaic);
        menuDisplayFields.add(DisplayFieldData.maxrMosaic);
        menuDisplayFields.add(DisplayFieldData.bMosaic);
        menuDisplayFields.add(DisplayFieldData.lMosaic);
        menuDisplayFields.add(DisplayFieldData.gageOnly);
        menuDisplayFields.add(DisplayFieldData.mMosaic);
        menuDisplayFields.add(DisplayFieldData.mlMosaic);
        menuDisplayFields.add(DisplayFieldData.satPre);
        if (includeGoesRPrecip) {
            menuDisplayFields.add(DisplayFieldData.goesRSatPre);
        }
        menuDisplayFields.add(DisplayFieldData.lsatPre);
        menuDisplayFields.add(DisplayFieldData.srMosaic);
        menuDisplayFields.add(DisplayFieldData.sgMosaic);
        menuDisplayFields.add(DisplayFieldData.srgMosaic);
        menuDisplayFields.add(DisplayFieldData.p3lMosaic);
        menuDisplayFields.add(DisplayFieldData.qmosaic);
        menuDisplayFields.add(DisplayFieldData.lqmosaic);
        menuDisplayFields.add(DisplayFieldData.mlqmosaic);
        menuDisplayFields.add(DisplayFieldData.rdMosaic);
        menuDisplayFields.add(DisplayFieldData.avgrdMosaic);
        menuDisplayFields.add(DisplayFieldData.maxrdMosaic);
        menuDisplayFields.add(DisplayFieldData.bdMosaic);
        menuDisplayFields.add(DisplayFieldData.ldMosaic);
        menuDisplayFields.add(DisplayFieldData.mdMosaic);
        menuDisplayFields.add(DisplayFieldData.mldMosaic);
        menuDisplayFields.add(DisplayFieldData.srdMosaic);
        menuDisplayFields.add(DisplayFieldData.srdgMosaic);
        menuDisplayFields.add(DisplayFieldData.localField1);
        menuDisplayFields.add(DisplayFieldData.localField2);
        menuDisplayFields.add(DisplayFieldData.localField3);
        menuItems = menuDisplayFields.toArray(new DisplayFieldData[0]);

        textMap.put(DisplayFieldData.rMosaic,
                new MenuData("Radar Mosaic", "R"));
        textMap.put(DisplayFieldData.avgrMosaic,
                new MenuData("Average Radar Mosaic", "A"));
        textMap.put(DisplayFieldData.maxrMosaic,
                new MenuData("Max Radar Mosaic", "x"));
        textMap.put(DisplayFieldData.bMosaic,
                new MenuData("Field Bias Radar Mosaic", "F"));
        textMap.put(DisplayFieldData.lMosaic,
                new MenuData("Local Bias Radar Mosaic", "L"));
        textMap.put(DisplayFieldData.gageOnly,
                new MenuData("Gage Only Analysis", "G"));
        textMap.put(DisplayFieldData.mMosaic,
                new MenuData("Multisensor Mosaic", "M"));
        textMap.put(DisplayFieldData.mlMosaic,
                new MenuData("Local Bias Multisensor Mosaic", "a"));
        textMap.put(DisplayFieldData.satPre,
                new MenuData("Satellite Precip", "S"));
        if (includeGoesRPrecip) {
            textMap.put(DisplayFieldData.goesRSatPre,
                    new MenuData("Satellite Precip (GOES-R)", "P"));
        }
        textMap.put(DisplayFieldData.lsatPre,
                new MenuData("Local Bias Satellite Precip", "o"));
        textMap.put(DisplayFieldData.srMosaic,
                new MenuData("Satellite Radar Mosaic", "e"));
        textMap.put(DisplayFieldData.sgMosaic,
                new MenuData("Satellite Gage Mosaic", "t"));
        textMap.put(DisplayFieldData.srgMosaic,
                new MenuData("Satellite Radar Gage Mosaic", "l"));
        textMap.put(DisplayFieldData.p3lMosaic,
                new MenuData("Triangulated Local Bias Mosaic", "T"));
        textMap.put(DisplayFieldData.qmosaic, new MenuData("Q2 Mosaic", "2"));
        textMap.put(DisplayFieldData.lqmosaic,
                new MenuData("Q2 Local Bias Mosaic", "B"));
        textMap.put(DisplayFieldData.mlqmosaic,
                new MenuData("Q2 Multi-sensor Mosaic", "i"));

        textMap.put(DisplayFieldData.rdMosaic,
                new MenuData("DP Radar Mosaic", "3"));
        textMap.put(DisplayFieldData.avgrdMosaic,
                new MenuData("DP Avg Radar Mosaic", "4"));
        textMap.put(DisplayFieldData.maxrdMosaic,
                new MenuData("DP Max Radar Mosaic", "5"));
        textMap.put(DisplayFieldData.bdMosaic,
                new MenuData("DP Field Bias Radar Mosaic", "6"));
        textMap.put(DisplayFieldData.ldMosaic,
                new MenuData("DP Local Bias Radar Mosaic", "7"));
        textMap.put(DisplayFieldData.mdMosaic,
                new MenuData("DP Field Bias Multisensor Radar Mosaic", "8"));
        textMap.put(DisplayFieldData.mldMosaic,
                new MenuData("DP Local Bias Multisensor Radar Mosaic", "9"));
        textMap.put(DisplayFieldData.srdMosaic,
                new MenuData("DP Satellite Radar Mosaic", "0"));
        textMap.put(DisplayFieldData.srdgMosaic,
                new MenuData("DP Satellite Radar Gage Mosaic", "1"));

        textMap.put(DisplayFieldData.localField1,
                new MenuData("Local Field #1", "d"));
        textMap.put(DisplayFieldData.localField2,
                new MenuData("Local Field #2", "f"));
        textMap.put(DisplayFieldData.localField3,
                new MenuData("Local Field #3", "O"));
    }

    @Override
    protected Map<DisplayFieldData, MenuData> getTexMap() {
        return PrecipFieldsPopulator.textMap;
    }

    @Override
    protected DisplayFieldData[] getMenuItems() {
        return PrecipFieldsPopulator.menuItems;
    }

    @Override
    protected MenuManager getMenuManger() {
        return PrecipFieldsPopulator.menuMgr;
    }

}
